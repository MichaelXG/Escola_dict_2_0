class Professor:
    def __init__(self
               , Matricula      : str
               , Nome           : str
               , Idade          : int
               , Disciplinas    : list = None):
        self.__Matricula    = Matricula
        self.__Nome         = Nome
        self.__Idade        = Idade
        self.__Disciplinas  = Disciplinas

    # Getters
    @property 
    def Matricula(self): 
        return self.__Matricula
    
    @property 
    def Nome(self): 
        return self.__Nome			
    
    @property 
    def Idade(self): 
        return self.__Idade			
   
    @property 
    def Disciplinas(self): 
        return self.__Disciplinas

    # Setters     
    @Matricula.setter 
    def Matricula(self, new_Matricula): 
        self.__Matricula = new_Matricula			
    
    @Nome.setter 
    def Nome(self, new_Nome): 	
        self.__Nome = new_Nome
     
    @Idade.setter
    def Idade(self, new_Idade):   
        self.__Idade = new_Idade
 
    @Disciplinas.setter
    def Disciplinas(self, new_Disciplinas):  
        self.__Disciplinas = new_Disciplinas
