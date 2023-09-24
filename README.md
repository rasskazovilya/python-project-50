### Hexlet tests and linter status:
[![Actions Status](https://github.com/rasskazovilya/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/rasskazovilya/python-project-50/actions)
[![Github Actions Status](https://github.com/rasskazovilya/python-project-50/workflows/test-lint/badge.svg)](https://github.com/rasskazovilya/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3552a23d5a02486f1426/maintainability)](https://codeclimate.com/github/rasskazovilya/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/3552a23d5a02486f1426/test_coverage)](https://codeclimate.com/github/rasskazovilya/python-project-50/test_coverage)

## Gendiff
Gendiff is an educational project from Hexlet Python Developer course. The main purpose of this script is to get difference between two `.json` or `.yaml` files. Output diff can be formatted in three ways:
- stylish - prints every (un)changed value line by line with a symbol to show, what changed, and appropriate indent for nested values.
- plain - prints readable messages for every change in files. Shows only changed lines.
- json - returns diff in json format.

### Requirements
- python > 3.8
- pip > 22.1
- poetry >= 1.5.1

### Installation
- Clone this repo  
```
git clone https://github.com/rasskazovilya/python-project-50
```
- Go to repo directory  
```
cd python-project-50
```
- Install, run tests and build package  
```
make install check build
```
### Usage
```
gendiff first_file second_file -f --format ['stylish', 'plain', 'json']
```
### Examples
#### Simple diff
- JSON  
[![asciicast](https://asciinema.org/a/S1jDFfYoGUoBkvDAyxyNzi3KW.svg)](https://asciinema.org/a/S1jDFfYoGUoBkvDAyxyNzi3KW)
- YAML  
[![asciicast](https://asciinema.org/a/1t0HqKjsCpXM9QCLDXGcsbGtu.svg)](https://asciinema.org/a/1t0HqKjsCpXM9QCLDXGcsbGtu)  
#### Nested diff with stylish format
[![asciicast](https://asciinema.org/a/dvJKbInJneIC1Oz3nqjNflCyg.svg)](https://asciinema.org/a/dvJKbInJneIC1Oz3nqjNflCyg)
#### Nested diff with plain format
[![asciicast](https://asciinema.org/a/bv4lcf7aj7iMxy0IMrsExSggW.svg)](https://asciinema.org/a/bv4lcf7aj7iMxy0IMrsExSggW)
#### Nested diff with json format
[![asciicast](https://asciinema.org/a/i526mOKdYiatWZzHem1YEM5BT.svg)](https://asciinema.org/a/i526mOKdYiatWZzHem1YEM5BT)
