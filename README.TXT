json-filter - Command-line JSON manipulation tool like JSONPath/XPath


                                            2012-12-06
                                            Ryoichi KATO <ryo1kato@gmail.com>

ABOUT
  A command line JSON query/filtering tool with JSONPath / XPath like
  notation ('DotDict' notation).

  Key difference are:
  - Keep original JSON structure as much as possible for output.
  - Implicit array expansion - You can ommit '[*]'
  - Shell like "name1.{name2a,name2b}.name3" and "name1.*.name3" expansion.
  - Conditions are NOT supported (yet)
  - CSV output is NOT implemented yet.


SEE ALSO
    http://goessner.net/articles/JsonPath/
