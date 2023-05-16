#@author Raine Troubetaris 
#@category Functions
#@keybinding 
#@menupath 
#@toolbar 

from pprint import pprint

func_manager = currentProgram.getFunctionManager()
funcs = func_manager.getFunctions(True)
func_refs = {}

for func in funcs:
    entry = func.getEntryPoint()
    refs = getReferencesTo(entry)
    #print refs
    callers = []
    for ref in refs:
        from_addr = ref.getFromAddress()
        #print from_addr
        if not func_manager.getFunctionContaining(from_addr) == None:
            calling_func = func_manager.getFunctionContaining(from_addr).getName()
            if calling_func not in callers:
                callers.append(calling_func)

    func_refs[func.getName()] = callers

pprint(func_refs)
