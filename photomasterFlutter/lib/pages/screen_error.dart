import 'package:flare_flutter/flare_actor.dart';
import 'package:flutter/material.dart';
import 'package:photomaster/widgets/background/im_bg_without_wave.dart';

class TelaError extends StatefulWidget {
  @override
  _TelaErrorState createState() => _TelaErrorState();
}

class _TelaErrorState extends State<TelaError> {
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 4)).then(
      (_) {
        Navigator.pop(context);
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: <Widget>[
          IMBGW(),
          Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Center(
                  child: Container(
                    height: 400,
                    child: FlareActor(
                      'assets/animation/load_and_check.flr',
                      animation: 'Error',
                    ),
                  ),
                ),
                Container(
                  height: 15,
                ),
                Text(
                  "Erro ao enviar, verifique sua conexão!",
                  style: TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
