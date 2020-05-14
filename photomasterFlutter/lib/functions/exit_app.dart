import 'dart:io';
import 'package:flutter/material.dart';

exitApp(context) {
  return showDialog(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: Text("Deseja sair do Aplicativo?"),
        actions: <Widget>[
          FlatButton(
            child: Text("Nao"),
            onPressed: () {
              Navigator.pop(context);
            },
          ),
          FlatButton(
            child: Text("Sim"),
            onPressed: () {
              exit(0);
            },
          ),
        ],
      );
    },
  );
}

returnScreen(context, tela) {
  return showDialog(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: Text("Deseja voltar?"),
        actions: <Widget>[
          FlatButton(
            child: Text("Nao"),
            onPressed: () {
              Navigator.pop(context);
            },
          ),
          FlatButton(
            child: Text("Sim"),
            onPressed: () {
              Navigator.of(context).pushReplacement(
                MaterialPageRoute(
                  builder: (context) => tela,
                ),
              );
            },
          ),
        ],
      );
    },
  );
}
