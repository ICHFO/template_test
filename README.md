Pre-requisites:
===============
Jinja2 python module:</br>
<code> pip install jinja2 </code>


Instructions:
=============
Scenario : I want to add and test a new template
-------------------------------------------------
1. Create the new template in the folder '/templates'
2. If the new template is expecting input data continue with step 3 otherwise skip to step 4
3. Add a TestData class for your template in the file '/test_data.py' (see Adding a TestData class)
4. Run `test_template.py <your_new_template_name>`

Adding a TestData class
-----------------------
If your new template extends from another template, your new class has to be a sub-class or the TestData class of the template you are extending.

Do not forget to add a mapping for te new TestData class in the class_dict at the bottom of test_data.py,
this dictionary is used to return the correct TestData class based on the template name.

example:

templates/new_template.html
```html
{% extends "resource.html" %}

{% block rescontent %}
Some HTML CODE here
{% endblock %}
```


test_data.py

```python
class Base_TestData(object):
  def __init__(self):
    self.data_dict = {}
    self.data_dict['get_flashed_messages']=get_flashed_messages
    return
		
  def get_data_dict(self):
    return self.data_dict
    
class Resource_TestData(Base_TestData):
  def __init__(self):
    # code to add items to the data_dict from Base_TestData goes here
    return
    
class New_Template_TestData(Resource_TestData):
  def __init__(self):
    # code to add items to the data_dict from Base_TestData goes here
    return

class_dict = {
  'base.html' : Base_TestData,
  'index.html' : Index_TestData,
  'resource.html' : Resource_TestData,
  'add_resource.html' : Add_Resource_TestData,
  'modify_resource.html': Modify_Resource_TestData,
  'resource_map.html' : Resource_Map_TestData,
  'new_template.html' : New_Template_TestData
}
```
