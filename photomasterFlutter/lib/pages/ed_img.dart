import 'dart:io';
import 'package:flutter/material.dart';
import 'package:photomaster/functions/exit_app.dart';
import 'package:photomaster/pages/telainicial.dart';

File file;

class ImageAfterPicker extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      child: Scaffold(
        appBar: AppBar(
          title: Text("Imagens"),
          centerTitle: true,
          elevation: 0,
          backgroundColor: Colors.black,
        ),
        body: Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.all(Radius.circular(15)),
          ),
          child: Center(
            child: Container(
              padding: EdgeInsets.all(8),
              child: Image.file(file),
            ),
          ),
        ),
        backgroundColor: Colors.black,
      ),
      onWillPop: () async {
        returnScreen(context, TelaInicial());
        return false;
      },
    );
  }
}
