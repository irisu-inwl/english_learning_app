import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


# TODO: mockはfileでいいんだけど、将来的にはデータをDBに溜めてランダムにしたりRandom or Searchで出せるようにしたい
# そうすれば、LLM = Generate+Recommendation という機能からデータが溜まった段階で Recommendation System として転換可能

def mock_reading_problem():
    with open("data/example.reading.yaml", "r") as rf:
        output_reading = rf.read()
    
    problem_reading = yaml.load(output_reading, Loader)
    return problem_reading


def mock_listening_problem():
    with open("data/example.listening.yaml", "r") as rf:
        output_listening = rf.read()
    
    problem_listening = yaml.load(output_listening, Loader)
    return problem_listening


def mock_writing_problem():
    with open("data/example.writing.yaml", "r") as rf:
        output_writing = rf.read()

    problem_writing = yaml.load(output_writing, Loader)

    return problem_writing
