from enum import Enum
class LogType(Enum):
    Create = 1
    Edit = 2
    Delete = 3
        
class RegisteredUser:
    def __init__(self, p_firstName, p_pwd):
        self.Name = p_firstName
        self.Pwd = p_pwd
        
class UserTask:
    def __init__(self, p_id, p_name, p_description, p_status):
        self.Id = p_id
        self.Name = p_name
        self.Description = p_description
        self.Status = p_status