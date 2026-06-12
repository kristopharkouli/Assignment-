import pytest
from score_processor import ScoreProcessor

@pytest.fixture
def processor():
    return ScoreProcessor()

def test_process_score_file_success(processor, tmp_path):
    valid_file = tmp_path / "score.txt"
    valid_file.write_text("42")
    assert processor.process_score_file(str(valid_file)) == 420

def test_process_score_file_invalid_format(processor, tmp_path):
    corrupt_file = tmp_path / "corrupt.txt"
    corrupt_file.write_text("abc")
    assert processor.process_score_file(str(corrupt_file)) == -1

def test_process_score_file_missing(processor):
    missing_path = "nonexistent_system_files_path/score.txt"
    assert processor.process_score_file(missing_path) == -1
