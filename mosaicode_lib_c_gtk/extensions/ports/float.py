from mosaicode.model.port import Port

class Float(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "FLOAT"
        self.color = "#fc2300"
        self.multiple = False
        self.code = "$input$ = $output$;\n"
        self.var_name = "$port[name]$$block[id]$"	
