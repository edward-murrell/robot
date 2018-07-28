# Robot

# Tests
All tests can be run by calling:
```
make tests
# OR
python3.6 -m unittest tests
```


## Unit
To run unit tests, use the following shell commands:
```
make unit.tests
# OR
python3.6 -m unittest tests.unit
```


# Assumptions
- No specific requirement was listed for when a `REPORT` command is given
 before a `PLACE` command is given. The following error is reported:
 `"Not on the board yet!`

# Limitations
- Board height & width can be zero, or negative.


# Credits
- Edward Murrell / edward@codefoundation.com.au
