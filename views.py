from flask import Flask, render_template, request, redirect, session, flash, url_for
from main import Corrente, Poupanca

app = Flask(__name__)
app. secret_key = 'bancocsv'

@app.route('/correntes')
def index():
    lista = Corrente.query.order_by(Corrente.id)
    return render_template('conta_corrente.html', titulo='Corrente', corrente=lista)

@app.route('/criar_corrente', methods=['POST',])
def criar():
    numero = request.form['numero']
    titular = request.form['titular']
    saldo = request.form['saldo']
    limite = request.form['limite']
   
    corrente = Corrente.query.filter_by(numero=numero).first()

    if corrente:
        flash("Conta já tem cadastro!")
        return redirect(url_for('index'))
    
    nova_corrente = Corrente(numero=numero, titular=titular, saldo=saldo, limite=limite)
    db.session.add(nova_corrente)
    db.session.commit()
   
    return redirect(url_for('index'))

@app.route('/poupanca')
def index():
    lista = Poupanca.query.order_by(Poupanca.id)
    return render_template('conta_poupanca.html', titulo='Poupanca', poupanca=lista)

@app.route('/criar_poupanca', methods=['POST',])
def criar():
    numero = request.form['numero']
    titular = request.form['titular']
    saldo = request.form['saldo']
   
    poupanca = Poupanca.query.filter_by(numero=numero).first()

    if poupanca:
        flash("Conta já tem cadastro!")
        return redirect(url_for('index'))
    
    nova_poupanca = Poupanca(numero=numero, titular=titular, saldo=saldo)
    db.session.add(nova_poupanca)
    db.session.commit()
   
    return redirect(url_for('index'))

@property
def numero(self, numero):
    self._numero = numero

@property
def saldo(self, saldo):
    self._saldo = saldo

def sacar(self, valor):
    self._saldo -= valor

def extrato(self):
    print("O saldo da conta é {} do titular {}. ".format(self._saldo, self._titular))

def depositar(self, valor):
    self._saldo += valor

def transferir(self, valor, destino):
    self.sacar(valor)
    destino.depositar(valor)
