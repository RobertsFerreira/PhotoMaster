import 'package:flutter/material.dart';
import 'package:photomaster/functions/exit_app.dart';
import 'package:photomaster/pages/telainicial.dart';
import 'package:photomaster/widgets/background/im_bg_without_wave.dart';

class IdentificaObjeto extends StatefulWidget {
  @override
  _IdentificaObjetoState createState() => _IdentificaObjetoState();
}

class _IdentificaObjetoState extends State<IdentificaObjeto> {
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
        child: Scaffold(
          body: Stack(
            children: <Widget>[
              IMBGW(),
            ],
          ),
        ),
        // onWillPop: () async {
        //   returnScreen(context, TelaInicial());
        //   return false;
        // }
        onWillPop: () async {
          return true;
        });
  }
}
