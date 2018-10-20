
from Rule import Rule

#段落的规则
class ParagraphRule(Rule):
    type = 'paragraph'
    def condition(self,block):
        return True