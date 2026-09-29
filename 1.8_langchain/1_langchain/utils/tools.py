from langchain_core.tools import tool
@tool
def get_module_deadline(module_name:str)->str:
    """ look up the submission deadline for the named bootcamp module

    Args:
    module_name: the module name eg: 'ANN', 'CNN', 'LLM'

    """
    deadline={
        "ANN":"2026-09-16",
        "CNN":"2026-09-17",
        "LLM":"2028-09-23"
    }

    return deadline.get(module_name, "No deadline found for that module")

@tool
def count_students_in_module(module_name:str)->str:
        """look up how many students are enrolled in a name bootcamp mdule"""
        counts={"ANN":24, "CNN":21, "LLM":34}
        return str(counts.get(module_name, 0))

# """ docstring is the description of what the tool is all about, its very very important because moduls what the tools is all about