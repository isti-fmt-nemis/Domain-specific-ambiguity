'''
Created on Sep 20, 2018

@author: alessioferrari
'''
from validation.generate_AMT_CSV_index import generate_CSV_from_index


term_list_top_bottom = dict()

'''
Min Frequency = 0.1
'''

# CS_EEN_top_f01 = ['channel', 'frequency', 'mode', 'interface', 'field', 'wave', 'theory', 'material', 'electron', 'database', 'science', 'solution', 'state', 'method', 'file', 'type', 'color', 'approach', 'quantum', 'conference']
# CS_EEN_step_f01 = ['database', 'frequency', 'field', 'power', 'component', 'network', 'display', 'input', 'solution', 'output', 'company', 'game', 'algorithm', 'management', 'form', 'language', 'bit', 'project', 'feature', 'problem']
# CS_MEN_top_f01 = ['program', 'user', 'particle', 'mass', 'software', 'version', 'load', 'tool', 'surface', 'access', 'security', 'feature', 'type', 'machine', 'service', 'operator', 'network', 'company', 'direction', 'device']
# CS_MEN_step_f01 = ['surface', 'program', 'software', 'engine', 'motion', 'management', 'area', 'operator', 'function', 'game', 'unit', 'project', 'input', 'technique', 'feature', 'approach', 'form', 'case', 'component', 'number']
# CS_MED_top_f01 = ['result', 'machine', 'theory', 'memory', 'device', 'function', 'interface', 'risk', 'database', 'cell', 'case', 'activity', 'response', 'example', 'effect', 'factor', 'level', 'area', 'approach', 'point']
# CS_MED_step_f01 = ['cell', 'result', 'function', 'procedure', 'processing', 'condition', 'program', 'level', 'application', 'person', 'access', 'tool', 'order', 'change', 'case', 'model', 'form', 'child', 'analysis', 'field']
# CS_SPO_top_f01 = ['access', 'design', 'goal', 'image', 'conference', 'network', 'security', 'tool', 'approach', 'theory', 'structure', 'service', 'school', 'hand', 'product', 'state', 'term', 'support', 'level', 'analysis']
# CS_SPO_step_f01 = ['security', 'network', 'theory', 'design', 'record', 'model', 'head', 'problem', 'space', 'process', 'source', 'hand', 'development', 'position', 'area', 'program', 'project', 'number', 'member', 'order']
# medical_software_top_f01 = ['risk', 'theory', 'function', 'interface', 'memory', 'result', 'cell', 'device', 'database', 'machine', 'factor', 'life', 'condition', 'engineering', 'support', 'college', 'case', 'type', 'response', 'management']
# medical_software_step_f01 = ['cell', 'result', 'function', 'procedure', 'processing', 'condition', 'program', 'level', 'application', 'person', 'access', 'tool', 'order', 'change', 'case', 'model', 'form', 'child', 'analysis', 'field']
# medical_device_top_f01 = ['wave', 'channel', 'cell', 'theory', 'frequency', 'interface', 'material', 'procedure', 'database', 'electron', 'level', 'hardware', 'science', 'processor', 'application', 'person', 'method', 'source', 'function', 'unit']
# medical_device_step_f01 = ['electron', 'channel', 'college', 'pressure', 'feature', 'practice', 'approach', 'image', 'color', 'service', 'development', 'model', 'space', 'hardware', 'source', 'state', 'technology', 'user', 'quantum', 'award']
# medical_robot_top_f01 = ['interface', 'database', 'activity', 'particle', 'tool', 'program', 'surface', 'procedure', 'electron', 'channel', 'access', 'wave', 'result', 'component', 'death', 'person', 'motion', 'order', 'problem', 'cell']
# medical_robot_step_f01 = ['surface', 'tool', 'motion', 'signal', 'material', 'series', 'rate', 'game', 'load', 'life', 'display', 'design', 'speed', 'support', 'protein', 'system', 'voltage', 'woman', 'conference', 'area']
# sport_rehab_machine_top_f01 = ['approach', 'effect', 'material', 'activity', 'college', 'tool', 'surface', 'wave', 'result', 'security', 'association', 'factor', 'test', 'foot', 'velocity', 'unit', 'speed', 'type', 'order', 'space']
# sport_rehab_machine_step_f01 = ['surface', 'activity', 'city', 'risk', 'database', 'structure', 'operation', 'bit', 'video', 'product', 'university', 'source', 'unit', 'system', 'application', 'output', 'company', 'exercise', 'web', 'range']

'''
Min Frequency = 0.3
'''
# CS_EEN_top_f03 = ['mode', 'tool', 'series', 'interface', 'hardware', 'component', 'theory', 'programming', 'video', 'field', 'work', 'time', 'feature', 'design', 'user', 'year', 'level', 'term', 'product', 'structure']
# CS_EEN_step_f03 = ['mode', 'video', 'series', 'software', 'input', 'solution', 'output', 'server', 'user', 'management', 'form', 'language', 'bit', 'project', 'feature', 'problem', 'state', 'award', 'conference', 'range']
# CS_MEN_top_f03 = ['area', 'theory', 'size', 'position', 'structure', 'field', 'operator', 'tool', 'development', 'service', 'design', 'source', 'point', 'company', 'term', 'image', 'time', 'control', 'machine', 'model']
# CS_MEN_step_f03 = ['tool', 'development', 'structure', 'area', 'position', 'function', 'group', 'image', 'machine', 'process', 'application', 'technique', 'feature', 'point', 'approach', 'design', 'form', 'system', 'case', 'technology']
# CS_MED_top_f03 = ['program', 'function', 'memory', 'result', 'solution', 'service', 'theory', 'image', 'device', 'condition', 'development', 'test', 'space', 'access', 'company', 'area', 'technology', 'management', 'school', 'science']
# CS_MED_step_f03 = ['memory', 'theory', 'device', 'solution', 'program', 'activity', 'level', 'university', 'access', 'development', 'order', 'management', 'method', 'case', 'test', 'model', 'process', 'form', 'technology', 'state']
# CS_SPO_top_f03 = ['product', 'case', 'rule', 'version', 'service', 'university', 'design', 'point', 'feature', 'conference', 'example', 'type', 'state', 'order', 'history', 'support', 'program', 'work', 'term', 'field']
# CS_SPO_step_f03 = ['conference', 'design', 'feature', 'case', 'rule', 'service', 'point', 'version', 'product', 'university', 'form', 'type', 'development', 'area', 'program', 'field', 'group', 'number', 'work', 'member']
# medical_software_top_f03 = ['theory', 'result', 'service', 'device', 'image', 'solution', 'program', 'function', 'condition', 'memory', 'source', 'field', 'order', 'activity', 'space', 'example', 'year', 'time', 'development', 'control']
# medical_software_step_f03 = ['memory', 'theory', 'device', 'solution', 'program', 'activity', 'level', 'university', 'access', 'development', 'order', 'management', 'method', 'case', 'test', 'model', 'process', 'form', 'technology', 'state']
# medical_device_top_f03 = ['result', 'program', 'device', 'memory', 'theory', 'function', 'solution', 'series', 'component', 'structure', 'state', 'term', 'group', 'technique', 'management', 'product', 'company', 'system', 'file', 'energy']
# medical_device_step_f03 = ['theory', 'series', 'program', 'material', 'rate', 'unit', 'mode', 'support', 'model', 'tool', 'test', 'network', 'type', 'machine', 'technology', 'game', 'university', 'day', 'school', 'processing']
# medical_robot_top_f03 = ['approach', 'theory', 'tool', 'surface', 'result', 'function', 'structure', 'series', 'device', 'motor', 'analysis', 'material', 'system', 'pressure', 'programming', 'temperature', 'range', 'award', 'direction', 'method']
# medical_robot_step_f03 = ['result', 'device', 'memory', 'stress', 'component', 'factor', 'model', 'response', 'system', 'support', 'test', 'water', 'hardware', 'software', 'condition', 'change', 'server', 'field', 'level', 'school']
# sport_rehab_machine_top_f03 = ['result', 'service', 'series', 'tool', 'feature', 'function', 'theory', 'device', 'material', 'surface', 'color', 'design', 'space', 'analysis', 'rule', 'load', 'work', 'term', 'age', 'university']
# sport_rehab_machine_step_f03 = ['result', 'surface', 'approach', 'image', 'side', 'order', 'case', 'body', 'energy', 'source', 'method', 'member', 'control', 'group', 'frequency', 'application', 'science', 'output', 'country', 'temperature']

'''
Terms generated with the approach that considers solely the most frequent terms of the different domains
'''

# CS_EEN_f03_w2vlen_100_dlen_200_top = ['cell', 'action', 'logic', 'sequence', 'surface', 'institute', 'table', 'line', 'format', 'particle', 'distribution', 'resource', 'design', 'access', 'state', 'core', 'video', 'source', 'pattern', 'storage']
# CS_MEN_f03_w2vlen_100_dlen_200_top = ['institute', 'theory', 'environment', 'distance', 'matrix', 'length', 'release', 'tool', 'law', 'frequency', 'business', 'distribution', 'output', 'issue', 'component', 'team', 'machine', 'concept', 'performance', 'approach']
# CS_MED_f03_w2vlen_100_dlen_200_top = ['device', 'performance', 'image', 'result', 'function', 'theory', 'content', 'memory', 'table', 'release', 'development', 'institute', 'test', 'class', 'field', 'society', 'signal', 'association', 'number', 'task']
# CS_SPO_f03_w2vlen_100_dlen_200_top = ['feature', 'rule', 'service', 'conference', 'pattern', 'table', 'case', 'design', 'technique', 'format', 'board', 'video', 'state', 'type', 'step', 'change', 'list', 'organization', 'university', 'element']
# medical_software_f03_w2vlen_100_dlen_200_top = ['performance', 'memory', 'result', 'theory', 'device', 'image', 'function', 'content', 'table', 'release', 'technique', 'error', 'case', 'work', 'condition', 'degree', 'level', 'professor', 'access', 'product']
# medical_device_f03_w2vlen_100_dlen_200_top = ['table', 'function', 'surface', 'sequence', 'theory', 'rule', 'result', 'chemical', 'library', 'pattern', 'game', 'graph', 'user', 'supply', 'technology', 'class', 'simulation', 'order', 'code', 'control']
# medical_robot_f03_w2vlen_100_dlen_200_top = ['environment', 'board', 'table', 'law', 'institute', 'value', 'pattern', 'surface', 'tool', 'chemical', 'area', 'server', 'heat', 'rule', 'solution', 'range', 'condition', 'issue', 'user', 'report']
# sport_rehab_machine_f03_w2vlen_100_dlen_200_top = ['surface', 'material', 'industry', 'law', 'result', 'contact', 'chemical', 'distance', 'table', 'pattern', 'april', 'approach', 'interaction', 'degree', 'structure', 'alternative', 'tree', 'engineering', 'june', 'journal']

#TEST: 
#[top_10 bottom_10] CS_MEN_f03_w2vlen_100_dlen_200_top = ['frequency', 'length', 'matrix', 'institute', 'release', 'tool', 'environment', 'law', 'theory', 'distance', 'problem', 'time', 'space', 'range', 'state', 'term', 'cost', 'year', 'example', 'test']
#TEST: min_occ = 800 
#CS_MEN_f03_w2vlen_100_dlen_200_top = ['hull', 'bar', 'room', 'option', 'argument', 'reduction', 'disk', 'interpretation', 'expression', 'house', 'year', 'link', 'phase', 'film', 'block', 'customer', 'transfer', 'order', 'report', 'distance']


'''
Terms generated with the approach that considers the terms that occur at least 800 times in each domain
'''
CS_EEN_f03_w2vlen_100_dlen_200_top = ['interpretation', 'formula', 'flash', 'relation', 'motor', 'bell', 'studio', 'contact', 'surface', 'news', 'capacity', 'solution', 'law', 'period', 'transfer', 'force', 'cycle', 'mapping', 'layer', 'output']
CS_MEN_f03_w2vlen_100_dlen_200_top = ['disk', 'room', 'expression', 'hull', 'reduction', 'option', 'bar', 'house', 'interpretation', 'argument', 'track', 'family', 'action', 'molecule', 'law', 'theory', 'life', 'production', 'source', 'tool']
CS_MED_f03_w2vlen_100_dlen_200_top = ['strength', 'editor', 'client', 'mouse', 'relation', 'matrix', 'pair', 'arm', 'argument', 'house', 'government', 'speech', 'word', 'germany', 'matter', 'success', 'community', 'transfer', 'location', 'class']
CS_SPO_f03_w2vlen_100_dlen_200_top = ['formula', 'loop', 'reduction', 'michael', 'founder', 'effect', 'string', 'washington', 'protein', 'statement', 'corporation', 'procedure', 'government', 'education', 'party', 'opportunity', 'selection', 'steve', 'interest', 'practice']
medical_software_f03_w2vlen_100_dlen_200_top = ['matrix', 'pair', 'house', 'arm', 'mouse', 'argument', 'editor', 'strength', 'relation', 'client', 'location', 'degree', 'university', 'science', 'principle', 'energy', 'production', 'fact', 'claim', 'statement']
medical_device_f03_w2vlen_100_dlen_200_top = ['interpretation', 'arm', 'expression', 'formula', 'argument', 'relation', 'consequence', 'client', 'house', 'surface', 'supply', 'desktop', 'authority', 'software', 'society', 'presence', 'byte', 'science', 'combination', 'provider']
medical_robot_f03_w2vlen_100_dlen_200_top = ['argument', 'expression', 'consequence', 'relation', 'institution', 'formula', 'respect', 'statement', 'father', 'ion', 'glass', 'partner', 'structure', 'laboratory', 'part', 'author', 'detector', 'message', 'sin', 'concept']
sport_rehab_machine_f03_w2vlen_100_dlen_200_top = ['founder', 'argument', 'brother', 'end', 'michael', 'consequence', 'story', 'ray', 'respect', 'statement', 'lack', 'context', 'complexity', 'practice', 'opening', 'panel', 'bike', 'experience', 'stage', 'rail']



'''
These dictionaries includes couples of "folder including the documents" : "inverted indexes stored in 
pkl files". Each dictionary is associated to a group of domains. 
'''

domain_list_CS_EEN = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl"}

domain_list_CS_MEN = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl"}
    
domain_list_CS_MED = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl"}    

domain_list_CS_SPO = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Sports_D_2" : "./INDEXES/SPO_dictionary.pkl"} 

domain_list_medical_device = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl"}

domain_list_medical_robot = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl"}

domain_list_sport_rehab = {"./DATASETS/Computer_Science_D_2": "./INDEXES/CS_dictionary.pkl", 
                      "./DATASETS/Electronic_Engineering_D_2": "./INDEXES/EEN_dictionary.pkl", 
                      "./DATASETS/Medicine_D_2" : "./INDEXES/MED_dictionary.pkl", 
                      "./DATASETS/Mechanical_Engineering_D_2": "./INDEXES/MEN_dictionary.pkl",
                      "./DATASETS/Sports_D_2" : "./INDEXES/SPO_dictionary.pkl"}


SENT_NUM = 3

if __name__ == '__main__':  
    
    generate_CSV_from_index(CS_EEN_f03_w2vlen_100_dlen_200_top, domain_list_CS_EEN, SENT_NUM, './CSV-AMT-Index/CS_EEN_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_MEN_f03_w2vlen_100_dlen_200_top, domain_list_CS_MEN, SENT_NUM, './CSV-AMT-Index/CS_MEN_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_MED_f03_w2vlen_100_dlen_200_top, domain_list_CS_MED, SENT_NUM, './CSV-AMT-Index/CS_MED_f03_w2vlen_100_dlen_200_top.csv') 
    generate_CSV_from_index(CS_SPO_f03_w2vlen_100_dlen_200_top, domain_list_CS_SPO, SENT_NUM, './CSV-AMT-Index/CS_SPO_f03_w2vlen_100_dlen_200_top.csv')
  
    generate_CSV_from_index(medical_device_f03_w2vlen_100_dlen_200_top, domain_list_medical_device, SENT_NUM, './CSV-AMT-Index/medical_device_f03_w2vlen_100_dlen_200_top.csv')
    generate_CSV_from_index(medical_robot_f03_w2vlen_100_dlen_200_top, domain_list_medical_robot, SENT_NUM, './CSV-AMT-Index/medical_robot_f03_w2vlen_100_dlen_200_top.csv')
    generate_CSV_from_index(sport_rehab_machine_f03_w2vlen_100_dlen_200_top, domain_list_sport_rehab, SENT_NUM, './CSV-AMT-Index/sport_rehab_machine_f03_w2vlen_100_dlen_200_top.csv')
     
    pass