import 'dart:io';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flare_flutter/flare_actor.dart';
import 'package:flutter/material.dart';
import 'package:photomaster/dados.dart';
import 'package:photomaster/pages/ed_img.dart';
import 'package:photomaster/pages/identificaObejto.dart';
import 'package:photomaster/pages/screen_error.dart';
import 'package:photomaster/pages/view_img.dart';

class LoadImg extends StatefulWidget {
  final File file;
  final String urlHttp;

  LoadImg({Key key, @required this.file, @required this.urlHttp})
      : super(key: key);
  @override
  _LoadImgState createState() => _LoadImgState(
        imgFile: file,
        caminho: urlHttp,
      );
}

class _LoadImgState extends State<LoadImg> {
  final File imgFile;
  final String caminho;
  _LoadImgState({Key key, @required this.imgFile, @required this.caminho});

  _enviarfoto(imagem) async {
    file = imagem;
    String url = "$urlMaster/$caminho";
    var bytes = file.readAsBytesSync();
    var response = await http.post(url,
        headers: {"Content-Type": "image/png"},
        body: bytes,
        encoding: Encoding.getByName("utf-8"));
    print(response.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: FutureBuilder(
        future: _enviarfoto(imgFile),
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
                        'assets/animation/load_and_check.flr',
                        animation: 'Loading',
                      ),
                    ),
                  ),
                  Container(
                    height: 15,
                  ),
                ],
              );
            default:
              if (snapshot.hasError) {
                return TelaError();
              } else {
                return TelaClose(path: caminho);
              }
          }
        },
      ),
    );
  }
}

class TelaClose extends StatefulWidget {
  final String path;
  TelaClose({Key key, @required this.path}) : super(key: key);
  @override
  _TelaCloseState createState() => _TelaCloseState(
        route: path,
      );
}

class _TelaCloseState extends State<TelaClose> {
  final String route;
  _TelaCloseState({Key key, @required this.route});
  @override
  void initState() {
    super.initState();
    Future.delayed(Duration(seconds: 2)).then((_) {
      Navigator.pop(context);
      if (route == "enviarfoto") {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ViewImage(),
          ),
        );
      }
      if (route == "caminho") {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => IdentificaObjeto(),
          ),
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
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
                'assets/animation/load_and_check.flr',
                animation: 'Success',
              ),
            ),
          ),
          Container(
            height: 15,
          )
        ],
      ),
    );
  }
}
