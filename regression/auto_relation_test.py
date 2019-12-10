import numpy as np
import matplotlib.pyplot as plt
class multiple_linear_regression(object):
    def __init__(self,y,X,*args):
        self.y = y
        self.X = X 
        self.name = args
        self.total_dict = {}
        self.OLS()
        self.iteration_method()
        try:
            self.first_order_difference()
        except:
            print('X is a singular matrix!')
    def regression(self,y,X):
        Beta = np.linalg.inv(((X-X.mean(axis = 0)).T.dot(X-X.mean(axis = 0)))).dot((X-X.mean(axis = 0)).T.dot((y - y.mean())))
        const = y.mean() - np.sum(X.mean(axis = 0)*Beta) 
        return {'cons':const,'coef':Beta}
    def pretty_report(self,type = 'OLS'):
        def get_regression_result(cons,coef,name):
            s = name[0] + ' = ' + str(cons)
#             print(ceof)
            for i in range(len(coef)):
                s += ' + ' + str(coef[i]) +'*'+ name[i+1] + '_' + str(i+1)
            return s
        template = \
"""
method: {type}
-------------------
{result}
DW_value: {DW}
rho: {rho}
error figure on each explanatory varible:
"""
        if type == 'OLS':
            name = self.name
        elif type == 'iteration_method':
            name = ['[{0}(t) - rho * {0}(t-1)]'.format(s) for s in self.name]     
        elif type == 'first_order_difference':
            name = ['delta_'+s for s in self.name]
#         para_dict = {}
#         print()
#         print(para_dict)
        para_dict = self.total_dict[type]
        format_dict = {'type':type,'result':get_regression_result(para_dict['cons'],para_dict['coef'],name),\
                      'DW':para_dict['DW'],'rho':para_dict['rho']}
        print(template.format(**format_dict))
        self.error_figure(type)
    def DW_test(self,type = 'OLS'):
        para_dict = self.total_dict[type]
        X,y,coef,cons = para_dict['X'],para_dict['y'],para_dict['coef'],para_dict['cons']
#         print(coef)
#         print(cons)
        error = X.dot(coef) + cons - y
        DW = np.sum(np.diff(error)**2) / np.sum(error[1:]**2)
        return {'error':error,'DW':DW,'rho': 1 - 0.5 * DW}
    def error_figure(self,type = 'OLS'):
        X,error = self.total_dict[type]['X'],self.total_dict[type]['error']
        for i in range(X.shape[1]):
                plt.figure()
                plt.scatter(X[:,i],error)
                plt.show()
    def OLS(self):
        self.total_dict['OLS'] = self.regression(self.y,self.X)
        self.total_dict['OLS'].update({'X':self.X,'y':self.y})
        self.total_dict['OLS'].update(self.DW_test('OLS'))
    def iteration_method(self):
        rho = self.total_dict['OLS']['rho']
        y,X = self.y[1:] - rho*self.y[:-1],self.X[1:,:] - rho*self.X[:-1,:]
        self.total_dict['iteration_method'] = {'y':y,'X':X}
        self.total_dict['iteration_method'].update(self.regression(y,X))
        self.total_dict['iteration_method'].update(self.DW_test('iteration_method'))
    def first_order_difference(self):
        y_diff = np.diff(self.y) 
        X_diff = np.diff(self.X,axis = 0)
        self.total_dict['first_order_difference'] = {'y':y_diff,'X':X_diff}
        self.total_dict['first_order_difference'].update(self.regression(y_diff,X_diff))
        self.total_dict['first_order_difference'].update(self.DW_test('first_order_difference'))