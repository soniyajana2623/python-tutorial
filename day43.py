# create virtual environment
python -m venv myenv

# activate the virtual environment
myenv\Scripts\activate

# deactivate the virtual environment
deactivate

# output the list of installed packages and their versions to a file
pip freeze > requirements.txt