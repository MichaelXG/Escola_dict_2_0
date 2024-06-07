class Funcionario:
    def __init__(self
               , Matricula  : str
               , Escola     : str
               , Nome       : str
               , Idade      : int
               , Cargo      : str
               ):
        
        self.__Matricula    = Matricula
        self.__Escola       = Escola
        self.__Nome         = Nome
        self.__Idade        = Idade
        self.__Cargo        = Cargo

    # Getters        
    @property 
    def Matricula(self): 
        return self.__Matricula								
    
    @property 
    def Escola(self): 
        return self.__Escola	
        
    @property 
    def Nome(self): 
        return self.__Nome			
    
    @property 
    def Idade(self): 
        return self.__Idade					

    @property 
    def Cargo(self): 
        return self.__Cargo

    # Setters     
    @Matricula.setter 
    def Matricula(self, new_Matricula): 
        self.__Matricula = new_Matricula			
    
    @Escola.setter
    def Escola(self, new_Escola): 
        self.Escola = new_Escola
        
    @Nome.setter 
    def Nome(self, new_Nome): 	
        if new_Nome is None:
            self.__Nome = None
        else:
            self.__Nome = new_Nome
     
    @Idade.setter
    def Idade(self, new_Idade):   
        self.__Idade = new_Idade

    @Cargo.setter
    def Cargo(self, new_Cargo):
        self.__Cargo = new_Cargo
