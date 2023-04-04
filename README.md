# Automated API tests for [Swagger Petstore](https://petstore.swagger.io/)
> Swagger Petstore is a sample Petstore server.

## Content:
- [Technology Stack](#technology-stack)
- [In a nutshell about the project](#in-a-nutshell-about-the-project)
- [Checks are implemented](#checks-are-implemented)
- Tests launch:
  - [Jenkins](#remote-launch-via-jenkins])
  - [Local](#local-launch )
- Reporst:
  - [Allure](#test-reports-available-in-allure)
  - [Allure TestOps](#intergation-with-allure-testops)
  - [Telegram](#telegram)
- [Video](#test-run-video-example)

## Technology Stack:
<div>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/python.png" title="Python" alt="Python" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/pycharm.png" title="PyCharm" alt="PyCharm" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/selene.png" title="Selene" alt="Selene" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/Jenkins.png" title="Jenkins" alt="Jenkins"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/selenoid.png" title="Selenoid" alt="Selenoid" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/Allure_Report.png" title="Allure Report" alt="Allure Report"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/AllureTestOps.png" title="AllureTestOps" alt="AllureTestOps"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/Jira.png" title="Jira" alt="Jira" width="40" height="40"/>
<img src="https://github.com/slazarska/petstore_api_test/blob/main/tests/resources/img/icons/Telegram.png" title="Telegram" alt="Telegram"/>
</div>

## In a nutshell about the project
- [x] Patterns `Page Object`
- [x] Self-documenting code
- [x] `Request/response` specification 
- [x] Parsing json files to access test data 
- [x] Remote launch using `Jenkins` and `Selenoid`
- [x] `Allure Reports` with attachments: logs, screenshots, videos
- [x] Logging requests/responses in `Allure Reports`
- [x] Integration with `Allure TestOps`
- [x] Integration with `Jira`
- [x] Notifications about test launch and test results via `Telegram`

## Checks are implemented:
- [X] - Successful/unsuccessful login and logout
- [X] - Creating and deleting a user
- [X] - Adding a new pet
- [X] - Update and deleting the pet

## Remote launch via [Jenkins](https://jenkins.autotests.cloud/job/slazarska-py-diplom-api/)

1. Click the "Build Now" button.
<p><img src="" alt="Jenkins"/></p>
## Run tests locally

## Local launch 

1. Clone the repository
2. Install Poetry (`poetry install`)
3. Open the project in PyCharm, add Python Interpreter
4. Create `env` files in the project folder according to the sample.
5. Run the tests in PyCharm or on the command line:
```bash
pytest . --alluredir allure-results/
```

#### *Allure Report is connected to build reports:*
![image]()
![image]()

> When running locally, enter:
```bash
allure serve .\allure-results
```

#### *Allure TestOps was used as a Test Management system:*
![image]()
![image]()
![image]()
<br />
<br />

#### *Integration with Jira:*
![image]()
<br /> 
<br />

#### *Telegram notification configured:*
![image]()
<br />
<br />

## Added video into tests run. Test run video example:
![video]()
<br><br>

Thanks :pray:<br/>
:green_heart: <a target="_blank" href="https://qa.guru">QA.GURU</a><br/>
:purple_heart: <a target="_blank" href="https://sites.google.com/view/qasisters/">QA Sisters</a><br/>
