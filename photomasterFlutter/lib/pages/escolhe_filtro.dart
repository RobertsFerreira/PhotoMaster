import 'package:flutter/material.dart';
import 'package:photomaster/widgets/background/img_bg.dart';
import 'dart:io';

class EscolheFiltro extends StatefulWidget {
  final File fileImage;

  EscolheFiltro({Key key, @required this.fileImage}) : super(key: key);
  @override
  _EscolheFiltroState createState() => _EscolheFiltroState(
        imageFile: fileImage,
      );
}

class _EscolheFiltroState extends State<EscolheFiltro> {
  final File imageFile;
  _EscolheFiltroState({Key key, @required this.imageFile});
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        return true;
      },
      child: Scaffold(
        body: Stack(
          children: <Widget>[
            IMGBG(),
            ListView(
              children: <Widget>[
                Container(
                  padding: EdgeInsets.only(
                    top: 80,
                    left: 10,
                    right: 10,
                  ),
                  child: SizedBox(
                    child: Image.file(imageFile),
                  ),
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: <Widget>[
                    Padding(
                      padding: EdgeInsets.only(
                        left: 15,
                        top: 80,
                      ),
                    ),
                  ],
                )
              ],
            ),
          ],
        ),
      ),
    );
  }
}
