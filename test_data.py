class Base_TestData(object):
	def __init__(self):
		self.data_dict = {}
		self.data_dict['get_flashed_messages']=get_flashed_messages
		return
		
	def get_data_dict(self):
		return self.data_dict
		
class Index_TestData(Base_TestData):
	def __init__(self):
		super().__init__()
		return
		
class Resource_TestData(Base_TestData):
	def __init__(self):
		super().__init__()
		return
		
class Add_Resource_TestData(Resource_TestData):
	def __init__(self):
		super().__init__()
		return
		
class Modify_Resource_TestData(Resource_TestData):
	def __init__(self):
		super().__init__()
		return
		
class Resource_Map_TestData(Resource_TestData):
	def __init__(self):
		super().__init__()
		return


def get_test_data(template_name):
	return data_dict.get(template_name)().get_data_dict()
	
data_dict = {
	'base.html' : Base_TestData,
	'index.html' : Index_TestData,
	'resource.html' : Resource_TestData,
	'add_resource.html' : Add_Resource_TestData,
	'modify_resource.html': Modify_Resource_TestData,
	'resource_map.html' : Resource_Map_TestData
}

def get_flashed_messages():
	return ''
