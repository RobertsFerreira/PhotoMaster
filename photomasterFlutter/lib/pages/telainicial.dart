import 'package:flutter/material.dart';
import 'package:photomaster/functions/exit_app.dart';
import 'package:photomaster/functions/image_picker.dart';
import 'package:photomaster/widgets/background/img_bg.dart';
import 'package:photomaster/widgets/buttons/button.dart';

import 'identificaObejto.dart';

class TelaInicial extends StatefulWidget {
  @override
  _TelaInicialState createState() => _TelaInicialState();
}

class _TelaInicialState extends State<TelaInicial> {
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
        child: Scaffold(
          body: Stack(
            children: <Widget>[
              IMGBG(),
              Container(
                padding: EdgeInsets.only(top: 100.0),
                child: Column(
                  children: <Widget>[
                    Center(
                      child: Text(
                        'PHOTO MASTER',
                        style: TextStyle(
                          // fontStyle: FontStyle.italic,
                          fontWeight: FontWeight.bold,
                          fontSize: 35.0,
                          color: Colors.white,
                        ),
                      ),
                    )
                  ],
                ),
              ),
              Container(
                padding: EdgeInsets.only(
                  top: 80.0,
                  left: 40,
                  right: 40,
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Center(
                      child: ButtonTelaInicial(
                          'Filtros para Fotos', Icons.filter, () async {
                        imagePicker(context);
                      }),
                    ),
                    Padding(
                      padding: EdgeInsets.only(top: 70.0),
                    ),
                    Center(
                      child: ButtonTelaInicial(
                          'Identificação de Objetos', Icons.camera, () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => IdentificaObjeto(),
                          ),
                        );
                      }),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        onWillPop: () async {
          exitApp(context);
          return false;
        });
  }
}
