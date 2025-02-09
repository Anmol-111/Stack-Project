import Bussiness_Entities.EMP_Entities as Bent
from Data_Access_Layer import EMP_DB as EDal
from Data_Access_Layer import Stack as SDal

obj_stack = SDal.Stack()
obj_db = EDal.Emp_db()

class Emp_Bal:

    def emp_insert_data(self, obj_ent: Bent.Emp_Entities):
        obj_stack.push(obj_ent)
        obj_db.connect_msserversql()
        obj_db.insert_data(obj_ent)

    def emp_retrieve_all_data(self):
        obj_db.connect_msserversql()
        data = obj_db.retrieve_all_data()
        if data:
            return data
        return "No data available."

    def emp_retrieve_data(self, emp_id):
        data = obj_stack.display_stack
        if data:
            for emp in data:
                if emp.get_emp_id() == emp_id:
                    return emp
        return "Employee not found."

    def emp_update_data(self, obj_ent=Bent.Emp_Entities()):
        obj_db.connect_msserversql()
        obj_db.update_data(obj_ent)

    def emp_delete_all_data(self):
        obj_stack.stack.clear()

    def emp_delete_id_data(self, emp_id):
        data = obj_stack.display_stack
        if data:
            for i, emp in enumerate(data):
                if emp.get_emp_id() == emp_id:
                    del obj_stack.stack[i]
                    return f"Employee with ID {emp_id} deleted."
        return "Employee not found."

    def auto_emp_id(self):
        obj_db.connect_msserversql()
        data=obj_db.retrieve_emp_id()
        return data+1

    def check_emp_id(self, obj_ent: Bent.Emp_Entities()):
        obj_db.connect_msserversql()
        data=obj_db.check_emp_id(obj_ent)
        return data