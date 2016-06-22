#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
李雷 lilei@qq.com"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.INGORECASE对大小写不敏感
regex = re.compile(pattern, flags=re.IGNORECASE)