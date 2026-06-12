class ScoreProcessor:
    def process_score_file(self, file_path: str) -> int:
        processed_result = -1

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                raw_score = int(file_content.strip())
                processed_result = raw_score * 10

        except FileNotFoundError:
            print(f"Error: The score file at '{file_path}' could not be found.")

        except ValueError:
            print("Error: File contains invalid data. Unable to parse text into an integer.")

        else:
            print("Data processed successfully")

        finally:
            print("File cleanup completed")

        return processed_result
