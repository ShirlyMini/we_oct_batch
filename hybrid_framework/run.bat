pytest -v -s TestCases --browser chrome --html=./Reports/sanity.html --capture=tee-sys -n=2 -m sanity
pytest -v -s TestCases --browser chrome --html=./Reports/functionality.html --capture=tee-sys -n=2 -m functionality
