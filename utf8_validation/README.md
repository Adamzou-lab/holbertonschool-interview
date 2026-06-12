# UTF-8 Validation

## Description

This project implements a UTF-8 encoding validator in Python. Given a list of integers (each representing one byte of data), the function determines whether the data represents a valid UTF-8 encoding.

## Requirements

- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)

## Task

### 0. UTF-8 Validation

**File:** `0-validate_utf8.py`

**Prototype:** `def validUTF8(data)`

- Returns `True` if `data` is a valid UTF-8 encoding, else `False`
- `data` is a list of integers, each representing 1 byte
- Only the 8 least significant bits of each integer are considered
- A UTF-8 character can be 1 to 4 bytes long

## UTF-8 Encoding Rules

| Bytes | Bit pattern |
|-------|-------------|
| 1     | `0xxxxxxx` |
| 2     | `110xxxxx 10xxxxxx` |
| 3     | `1110xxxx 10xxxxxx 10xxxxxx` |
| 4     | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

## Usage

```bash
./0-main.py
True
True
False
```

## Repository

- **GitHub:** holbertonschool-interview
- **Directory:** utf8_validation
