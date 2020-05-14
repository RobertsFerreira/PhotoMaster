import 'package:flare_flutter/flare_actor.dart';
import 'package:flutter/material.dart';
import 'package:photomaster/pages/telainicial.dart';
import 'package:http/http.dart' as http;

class Splash extends StatefulWidget {
  @override
  _SplashState createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  _recebeTeste() async {
    String url = "http://robertferreira.ddns.net:5000/teste";
    var response = await http.get(url);
    print(response.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: FutureBuilder(
        future: _recebeTeste(),
        builder: (context, snapshot) {
          switch (snapshot.connectionState) {
            case ConnectionState.none:
            case ConnectionState.waiting:
              return Stack(
                children: <Widget>[
                  Container(
                    padding: EdgeInsets.fromLTRB(10, 20, 10, 20),
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        stops: [0.1, 1.2],
                        colors: [
                          Color(0xFFF92B7F),
                          Color(0xFFF58524),
                        ],
                      ),
                    ),
                    child: Center(
                      child: FlareActor(
                        'assets/animation/load_start.flr',
                        animation: 'active',
                      ),
                    ),
                  ),
                  Column(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: <Widget>[
                      Center(
                        child: Text(
                          "Developed by Robert Ferreira",
                          style: TextStyle(
                            color: Colors.black,
                            fontWeight: FontWeight.w300,
                            fontSize: 15,
                          ),
                        ),
                      ),
                      Container(
                        height: 15,
                      )
                    ],
                  ),
                ],
              );
            default:
              if (snapshot.hasError) {
                return Center(child: Text("Erro ao acessar"));
              } else {
                return TelaInicial();
              }
          }
        },
      ),
    );
  }
}
