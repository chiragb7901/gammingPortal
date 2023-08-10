from app.main.models import Role


class RoleService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_role_data():
        role_entities = Role.query.all()
        role_entities_list = []
        
        for user in role_entities:
            role_dict = {}
            role_dict['id'] = user.id
            role_dict['role'] = user.role
            role_dict['created_at'] = user.created_at
            role_dict['updated_at'] = user.updated_at
           
            role_entities_list.append(role_dict)
        return role_entities_list

    @staticmethod
    def get_role_by_id(id):
        role_entities = Role.query.filter_by(id=id)
        role_entities_list = []

        for user in role_entities:
            role_dict = {}
            role_dict['id'] = user.id
            role_dict['role'] = user.role
            role_dict['created_at'] = user.created_at
            role_dict['updated_at'] = user.updated_at

            role_entities_list.append(role_dict)
        return role_entities_list
    


    @staticmethod
    def save_new_role(data):

        new_role = Role(
                role=data["role"]
        )
        new = Role.create(new_role)
        response_object = {
                "status": "success",
                "object":{
                    "role":new.role,
                    "id":new.id

                },
                "message": "Successfully added.",
        }
        return response_object, 201

        

    @staticmethod
    def delete_role(id):
        role= Role.query.filter_by(id=id).first()
        
        if role:
            Role.delete(role)
            response_object = {
                "status": "success",
                "message": "Successfully deleted.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "role does not exists.",
            }
            return response_object, 409     

    @staticmethod
    def update_role(id,data):
        
        roleNew = Role.query.filter_by(id=id).first()

    
        if roleNew:

            roleNew.role = data.get('role', roleNew.role)

            new = Role.update(roleNew)
            response_object = {
                "status": "success",
                "object":{
                    "role":new.role,
                    "id":new.id

                },
                "message": "Successfully updated.",
            }
            return response_object, 201
        else:
            response_object = {
                "status": "fail",
                "message": "Card does not exists.",
            }
            return response_object, 409

