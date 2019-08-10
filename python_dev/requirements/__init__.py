import os
import os.path

class Requirement(object):
    def __init__(self, line=None, **kw):
        if line:
            if '--hash' in line:
                self.hash = line.split('--hash')[1].strip()[1:].strip()
                line = line.split('--hash')[1].strip()
            if '~=' in line:
                self.package = line.split('~=')[0].strip()
                self.version = line.split('~=')[1].strip()
                self.operator = '~='
            if '==' in line:
                self.package = line.split('==')[0].strip()
                self.version = line.split('==')[1].strip()
                self.operator = '=='
            elif '>=' in line:
                self.package = line.split('>=')[0].strip()
                self.version = line.split('>=')[1].strip()
                self.operator = '>='
            elif '<=' in line:
                self.package = line.split('<=')[0].strip()
                self.version = line.split('<=')[1].strip()
                self.operator = '<='
            elif '>' in line:
                self.package = line.split('>')[0].strip()
                self.version = line.split('>')[1].strip()
                self.operator = '>'
            elif '<' in line:
                self.package = line.split('<')[0].strip()
                self.version = line.split('<')[1].strip()
                self.operator = '<'
            else:
                self.package = line.strip()
                self.version = None
                self.operator = None
        else:
            self.package = kw.get('package')
            self.version = kw.get('version')
            self.operator = kw.get('operator')
            self.hash = kw.get('hash')
        self.upper_operator = None
        self.upper_version = None
        self.hash = None
        if self.version and ',' in self.version:
            upper_bound = self.version.split(',')[1].strip()
            self.version = self.version.split(',')[0].strip()
            if '<=' == upper_bound[:2]:
                self.upper_operator = '<='
                self.upper_version = upper_bound[2:].strip()
            elif '<' == upper_bound[0]:
                self.upper_operator = '<'
                self.upper_version = upper_bound[1:].strip()
                
    def line(self):
        line = self.package
        if self.operator:
            line = line+self.operator
        if self.version:
            line = line+self.version
        if self.upper_operator:
            line = line+','+self.upper_operator
        if self.upper_version:
            line = line+self.upper_version
        if self.hash:
            line = line+' --hash='+self.hash
        return line
    
    def install(self):
        from pip._internal import main as pipmain
        call = ['install']
        call.extend(self.line().split())
        pipmain(call)
                                
            
            
class Comment(object):
    def __init__(self, line):
        self.comment = line
        
    def line(self):
        return self.comment
        
class Option(object):
    def __init__(self, line):
        self.option = line.split('=')[0].strip()[2:]
        self.value = line.split('=')[1].strip()
        
    def line(self):
        return '--{opt}={val}'.format(opt=self.option, val=self.value)
        
class Requirements(object):
    def __init__(self):
        self.lines = []
        self.options = []
        self.requirements = []
        
    def add(self, item):
        if isinstance(item, Option):
            self.options.append(item)
        if isinstance(item, Requirement):
            self.requirements.append(item)
        self.lines.append(item)
        
    def includes(self, package):
        return package in [r.package for r in self.requirements]
    
    def write(self, requirements_txt):
        if not os.path.exists(requirements_txt):
            open(requirements_txt, 'w').close()
        with open(requirements_txt, 'w') as fp:
            for item in self.lines:
                fp.write(item.line()+os.linesep)
   
        

def get_requirements(requirements_txt):
    if not os.path.exists(requirements_txt):
        open(requirements_txt, 'w').close()
    with open(requirements_txt, 'r') as fp:
        lines = fp.readlines()
    requirements = Requirements()
    for line in lines:
        if len(line.strip()) == 0 or line.strip()[0] == '#':
            requirements.add(Comment(line))
        elif line.strip()[:2] == '--':
            requirements.add(Option(line))
        else:
            requirements.add(Requirement(line))
    return requirements
        
    

def add_requirement(package, version=None, operator=None, hash=None):
    from python_dev import pyde
    requirements_txt = os.path.sep.join([pyde.install_dir, 'requirements.txt'])
    requirements = get_requirements(requirements_txt)
    if not requirements.includes(package):
        requirement = Requirement(package=package, version=version, operator=operator, hash=hash)
        requirements.add(requirement)
        print('Adding requirement: {req}'.format(req=requirement.line()))
        requirements.write(requirements_txt)
        requirement.install()
    else:
        print('{package} is already required'.format(package=package))
    
    

    