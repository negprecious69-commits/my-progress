from langchain_core.tools import tool

#tool for looking up submission deadline for a named module
@tool
def module_ deadline_ lookup(module_name:str) -> str:
    """look up the submission deadline for a named course
    Args:
        course_name: the name of the course eg 'physice', 'maths', 'statistics'
    """
    deadlines={
        'physics': "2026-09-16",
        'maths': "2026-10-17",
        'statistics': "2026-11-23"
    }

    return deadlines.get (module_name, 'No deadline found for that course')

#tool for counting students in a module
@tool
def student count_ lookup(module_name:str) -> int:
    "look up how many students are enrolled in a named module'
    counts = ('physics':55, 'maths': 77, 'statistics': 42)
    return counts.get ( module name, 'student not found')

#which tool must be completed before which
@tool
def prereguisite(tool_ name:int) -> int:
    "look up which too1 must be completed before which"
    prerequisities={
         'physics': '1',
        'maths': '2',
        'statistics':'3'
        }
    return preguisite.get(tool_name, "prerequisite not found")

#session for a specific name module
@tool
def session_module_lookup(module_name:str) -> str:
    "look up the room and schedule for a specific named module"
    session = {
        "physics":"Block 17",
        "maths":"ppb02",
        "statistics":"amphi 650"
    }        
    return session.get(module_name, "Module not found")