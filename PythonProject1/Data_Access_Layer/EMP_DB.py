import Bussiness_Entities.EMP_Entities as Bent
import Data_Access_Layer.Stack as Dal
import pymssql
class Emp_db:
    def connect_msserversql(self):
        global constr
        global cursor
        constr = pymssql.connect(server="LAPTOP-8T8MA06J\\SQLEXPRESS",
                                 user="root",
                                 password="Admin@1234",
                                 database="emp_stack_db")
        cursor= constr.cursor()
    def insert_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_insert_data', (obj_stack.get_emp_id(), obj_stack.get_name(),obj_stack.get_age(),obj_stack.get_salary(),obj_stack.get_designation()))
        constr.commit()

    def retrieve_all_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_retrieve_all_data')
        data = cursor.fetchall()
        return data

    def retrieve_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_retrieve_id_data', (obj_stack.get_emp_id(),))

    def update_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_update_data', (obj_stack.get_emp_id(),obj_stack.get_name(),obj_stack.get_age(),obj_stack.get_salary(),obj_stack.get_designation()))
        constr.commit()

    def delete_all_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_delete_all_data')
        constr.commit()

    def delete_id_data(self, obj_stack=Dal.Stack()):
        cursor.callproc('sp_delete_id_data', (obj_stack.get_emp_id(),))
        constr.commit()

    def retrieve_emp_id(self):
        cursor.callproc('sp_retreive_emp_id')
        data=cursor.fetchone()
        return int(data[0])

    def check_emp_id(self, obj_ent=Bent.Emp_Entities()):
        cursor.execute('SELECT EMP_ID FROM emp WHERE EMP_ID=%s', (obj_ent.get_emp_id(),))
        data=cursor.fetchall()
        return data