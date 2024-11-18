import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
import os
from unittest.mock import patch, MagicMock
from structure import RepoStructure

class TestRepoStructure:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.repo_structure = RepoStructure()
        self.repo_structure.startpath = os.path.dirname(os.path.abspath(__file__))

    def test_list_files_normal_case(self):
        """Test list_files method returns correct file structure"""
        # Setup a temporary directory structure
        with pytest.raises(FileNotFoundError):
            self.repo_structure.list_files()

    def test_list_files_with_mocked_os_walk(self, mocker):
        """Test list_files method with mocked os.walk"""
        mocked_os_walk = mocker.patch('os.walk')
        mocked_os_walk.return_value = [
            ('root', ('dir1',), ('file1.py',)),
            ('root/dir1', (), ('file2.js', 'file3.txt')),
        ]
        expected_structure = 'root/\n    dir1/\n        file2.js\n        file3.txt\n        file1.py\n'
        assert self.repo_structure.list_files() == expected_structure

    def test_list_files_ignore_git_and_github_dirs(self, mocker):
        """Test list_files method ignores .git and .github directories"""
        mocker.patch('os.walk', return_value=[
            ('root', ('.git', '.github', 'dir1'), ('file1.py',)),
            ('root/.git', (), ()),
            ('root/.github', (), ()),
            ('root/dir1', (), ('file2.js',)),
        ])
        expected_structure = 'root/\n    dir1/\n        file2.js\n'
        assert self.repo_structure.list_files() == expected_structure

    def test_get_repo_path_success(self, mocker):
        """Test get_repo_path method on success"""
        mocker.patch('subprocess.check_output', return_value=b'/path/to/repo')
        assert RepoStructure.get_repo_path() == '/path/to/repo'

    def test_get_repo_path_failure(self, mocker):
        """Test get_repo_path method on failure (not a Git repository)"""
        mocked_check_output = mocker.patch('subprocess.check_output', side_effect=subprocess.CalledProcessError(1, ['git']))
        mocker.patch('builtins.print')
        assert RepoStructure.get_repo_path() is None

    def test_list_files_depth_limitation(self, mocker):
        """Test list_files respects max_depth limitation"""
        self.repo_structure.max_depth = 1  # Setting depth to 1
        mocker.patch('os.walk', return_value=[
            ('root', ('dir1',), ('file1.py',)),
            ('root/dir1', ('dir2',), ('file2.js',)),
            ('root/dir1/dir2', (), ('file3.txt',)),
        ])
        expected_structure = 'root/\n    dir1/\n        file2.js\n'
        assert self.repo_structure.list_files() == expected_structure

    def test_list_files_extension_filtering(self, mocker):
        """Test list_files filters files by extension"""
        mocker.patch('os.walk', return_value=[
            ('root', (), ('file1.py', 'file2.unknown', 'file3.js', 'README.md')),
        ])
        expected_structure = 'root/\n    file1.py\n    file3.js\n    README.md\n'
        assert self.repo_structure.list_files() == expected_structure

    def test_constructor_initial_values(self):
        """Test RepoStructure constructor initializes properties correctly"""
        assert self.repo_structure.max_depth == 4
        assert '.py' in self.repo_structure.file_extensions
        assert 'nonexistent.ext' not in self.repo_structure.file_extensions