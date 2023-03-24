import re

text = '''
Contents
1 The vision 1
2 Background to MISRA C 2
2.1 The popularity of C 2
2.2 Disadvantages of C 2
2.3 The use of C in critical systems 3
3 Tool selection 4
3.1 The C language and its compiler 4
3.2 Analysis tools 5
4 Prerequisite knowledge 6
4.1 Training 6
4.2 Understanding the compiler 6
4.3 Understanding the static analysis tools 6
5 Adopting and using MISRA C 8
5.1 Adoption 8
5.2 Software development process 8
5.3 Compliance 9
5.4 Deviation procedure 11
5.5 Claiming compliance 12
6 Introduction to the guidelines 13
6.1 Guideline classification 13
6.2 Guideline categories 13
6.3 Organization of guidelines 14
6.4 Redundancy in the guidelines 14
6.5 Decidability of rules 14
6.6 Scope of analysis 15
6.7 Multi-organization projects 15
6.8 Automatically generated code 16
6.9 Presentation of guidelines 17
6.10 Understanding the source references 18
7 Directives 21
7.1 The implementation 21
7.2 Compilation and build 23
7.3 Requirements traceability 23
7.4 Code design 24
8 Rules 38
8.1 A standard C environment 38
8.2 Unused code 40
8.3 Comments 46
8.4 Character sets and lexical conventions 47
8.5 Identifiers 49
8.6 Types 59
8.7 Literals and constants 60
8.8 Declarations and definitions 64
8.9 Initialization 76
8.10 The essential type model 82
8.11 Pointer type conversions 95
8.12 Expressions 104
8.13 Side effects 110
8.14 Control statement expressions 117
8.15 Control flow 124
8.16 Switch statements 132
8.17 Functions 138
8.18 Pointers and arrays 145
8.19 Overlapping storage 155
8.20 Preprocessing directives 157
8.21 Standard libraries 167
8.22 Resources 182
9 References 193
Appendix A Summary of guidelines 195
Appendix B Guideline attributes 204
Appendix C Type safety issues with C 208
Appendix D Essential types 211
Appendix E Applicability to automatically generated code 217
Appendix F Process and tools checklist 220
Appendix G Implementation-defined behaviour checklist 221
Appendix H Undefined and critical unspecified behaviour 225
Appendix I Example deviation record 235
Appendix J Glossary 238
Appendix K Change log 242
'''

'''
页码前空白换成一个TAB
find    :(\w)(\s+)(\d+)
replace :$1	$3

二级标题前缩进一个TAB
find    :(^\d\.\d.*)
replace :	$1
'''


def page_add(match):
    # print(match.group())
    page = int(match.group()) + 8
    return '\t'+str(page)+'\n'
    # return '1\n'


if '__main__' == __name__:

    s = re.sub(r'\s+\d+\n', page_add, text)
    print(s)
