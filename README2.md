- A README file that details:
    - An overview of your project.
    - How to run your application locally.
    - How the CI pipeline works.
    - The tools and technologies used.

Overview: 
    This project is a project that has a module that prints hello world.  This project has 2 github actions.  The first github action is a linting github action, it makes sure that the python module conforms to PEP8 requirements.  The second github action is a github action to build an RPM package from the project.  The project also has a unit test.  

How to run your application locally:
    To run the application locally, if you have a CentOS system, you can run the github action, build RPM and it will create an RPM which you can download to your system and then use $rpm -i {rpm-name}.rpm after this you can run the package you installed with {rpm-name}.  If not you can download the tar.gz file, extract it with $tar -xvf, cd into the created directory and then run $python hello_world.py .  You will need to have python installed on your system.  

How the CI pipeline works:
    The CI pipeline has 2 files.  There is a pipeline to lint the python files, it runs when there is a pull request.  The other file creates an RPM, it runs when someone pushes to the develop branch of the project

The tools and technolgies used:
    This project uses github actions, python, rpm and spec files.  I used github codespaces to create and test the project
