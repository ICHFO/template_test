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
4. Run `python test_template.py <your_new_template_name>`

Adding a TestData class
-----------------------
If your new template extends from another template, your new class has to be a sub-class or the TestData class of the template you are extending.

Do not forget to add a mapping for the new TestData class in the class_dict at the bottom of test_data.py,
this dictionary is used to return the correct TestData class based on the template name.



example:

templates/new_template.html
```html
{% extends "resource.html" %}

{% block rescontent %}
<!-- Using a simple variable in jinja2 template -->
<p> This is the value of the simple variable : {{ simple_var }} </p>


<!-- using a more complex variable (dictionary) in jinja2 template -->
<!-- fetching a single element from dictionay -->
<p> This is the value of the 2nd dictionary element : {{ dict_var.get('mnd_var2') }} </p

<!-- looping over the dictionary -->
{% for k,v in dict_var.items() %}
	<p> The value for dictionary key {{ k }} equals {{ v }} </p>
{% endfor %}

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
    super().__init__()
    # code to add items to the data_dict from Base_TestData goes here
    return
    
class New_Template_TestData(Resource_TestData):
  def __init__(self):
    super().__init__()
    # add a simple variable to the data_dict
    self.data_dict['simple_var'] = "Hallo daar!"
    # add a more complex variable (dictionary) to the data_dict
    my_new_dict = { 'mnd_var1' : 'dict var 1', 'mnd_var2' : 3, 'mnd_var3' : 3.5 }
    self.data_dict['dict_var'] = my_new_dict
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
