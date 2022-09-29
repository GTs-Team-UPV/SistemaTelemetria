from sklearn import linear_model

"""Inteligencia artificial de calculo de regresion lineal
Para usarlo se necesita la libreria sklearn
    Tiene 3 metodos principales:

    añdirDatos(list() Y, list() X, int valor_maximo_de_Y)
    Este metodo pone en entrenamiento la inteligencia artificial y crea el coeficiente y el modulo del la ecuacion lineal
    atributos, este metodo se puede usar varias veces para ajustar el entrenamiento contra mas datos mas precision
    valorMaximoY sirve para ajustar la linea a un X=0 para poder decir por ejemplo que en tiempo 0 el valor es 100 o 98
     o lo que sea para que la interpretacion sea mas entendible

     predecirY(list() valor a predecir)
     este metodo usa el coeficiente y el modulo para calcular que valor de Y tendria cierto X,
     se pueden predecir cuantos datos se requeriera ya que el atributo es un list()

     predecirX(list() valor a predecir)
     es similar a predecirY pero este le das un valor Y y teda un X, es muy util para saber cuando sera 0% por ejemplo"""


class Predictor:
    def __init__(self):
        self.coef = 0
        self.offset = 0
        self.regr = linear_model.LinearRegression()
        return

    def añadirDatos(self, porc, t, valorMaximoY=None):
        porcentaje = porc.copy()
        tiempo = t.copy()
        if valorMaximoY != None:
            self.regr.fit_intercept = False
            for i in range(0, len(porcentaje), 1):
                porcentaje[i] = porcentaje[i] - valorMaximoY
        for i in range(0, len(tiempo), 1):
            tiempo[i] = [0, tiempo[i]]
        self.regr.fit(tiempo, porcentaje)
        self.regr.fit_intercept = True
        self.coef = self.regr.coef_[1]
        if valorMaximoY == None:
            self.offset = self.regr.intercept_
            return
        self.offset = valorMaximoY
        return

    def __str__(self):
        return "y = {} * x + {}".format(str(self.coef), str(self.offset))

    def get_coef(self):
        return self.coef

    def get_offset(self):
        return self.offset

    def predecirX(self, pred):
        prec = pred.copy()
        newPorc = list()
        for i in range(0, len(prec), 1):
            newPorc.append((prec[i] - self.offset) / self.coef)
        return newPorc

    def predecirY(self, pred):
        prec = pred.copy()
        newPorc = list()
        for i in range(0, len(prec), 1):
            newPorc.append(self.coef * prec[i] + self.offset)
        return newPorc
