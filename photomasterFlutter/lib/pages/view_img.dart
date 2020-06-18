import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:photomaster/dados.dart';
import 'package:photomaster/widgets/background/img_bg.dart';
import 'package:dio/dio.dart';
import 'package:downloads_path_provider/downloads_path_provider.dart';

class ViewImage extends StatefulWidget {
  @override
  _ViewImageState createState() => _ViewImageState();
}

class _ViewImageState extends State<ViewImage> {
  String imagemFundo;
  String json;

  List listaimagens = [];

  _recebeLista() async {
    String url = "$urlMaster/lista";
    var response = await http.get(
      url,
    );
    json = response.body;

    List map = jsonDecode(json);

    listaimagens.clear();

    for (var m in map) {
      listaimagens.add(m["imagem"]);
    }
    setState(() {
      print("");
    });
  }

  @override
  void initState() {
    super.initState();

    setState(
      () {
        imageCache.clear();
        imagemFundo = "$urlMaster/receberfoto/original";
        _recebeLista();
      },
    );
  }

  _popUpImage(imagem, context) {
    setState(() {
      imagemFundo = imagem;
    });
  }

  _mostraFoto(imagem, context) {
    double _size = 44;
    return Container(
      padding: EdgeInsets.all(8),
      child: Column(
        children: <Widget>[
          ClipOval(
            // button color
            child: InkWell(
              splashColor: Colors.red, // inkwell color
              child: SizedBox(
                width: _size,
                height: _size,
                child: Image(
                  image: NetworkImage(imagem),
                  fit: BoxFit.cover,
                ),
              ),
              onTap: () {
                _popUpImage(imagem, context);
              },
            ),
          ),
          Text(
            imagem.toString().replaceAll("$urlMaster/receberfoto/", ""),
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
          Container(
            margin: EdgeInsets.only(top: 2),
            height: 5,
            width: 15,
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(5),
              color:
                  imagem == imagemFundo ? Colors.blue[300] : Colors.transparent,
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        return true;
      },
      child: Scaffold(
        appBar: AppBar(
          elevation: 0,
          title: Text(
            "Imagem Filtrada",
          ),
          backgroundColor: Color(0xFFF92B7F),
          centerTitle: true,
          actions: <Widget>[
            IconButton(
              icon: Icon(
                Icons.file_download,
                color: imagemFundo.replaceAll("$urlMaster/receberfoto/", "") ==
                        "original"
                    ? Colors.transparent
                    : Colors.white,
              ),
              onPressed:
                  imagemFundo.replaceAll("$urlMaster/receberfoto/", "") ==
                          "original"
                      ? null
                      : () async {
                          Map<Permission, PermissionStatus> statuses =
                              await [Permission.storage].request();
                          print(statuses);
                          final output =
                              await DownloadsPathProvider.downloadsDirectory;
                          Dio dio = Dio();
                          var response = await dio.download(imagemFundo,
                              "${output.path}/${imagemFundo.replaceAll('$urlMaster/receberfoto/', '')}.jpg");
                          print(response);
                          showDialog(
                              context: context,
                              builder: (BuildContext context) {
                                return AlertDialog(
                                  title: Text("Donwload Concluido!"),
                                  actions: <Widget>[
                                    FlatButton(
                                      onPressed: () {
                                        Navigator.pop(context);
                                      },
                                      child: Text("OK"),
                                    )
                                  ],
                                );
                              });
                        },
            ),
          ],
        ),
        body: Stack(
          children: <Widget>[
            IMGBG(),
            Center(
              child: Container(
                padding: EdgeInsets.all(10),
                child: Image.network(imagemFundo),
              ),
            ),
            Column(
              mainAxisAlignment: MainAxisAlignment.end,
              children: <Widget>[
                Center(
                  child: Container(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Color(0xFFF58524),
                          Color(0xFFF92B7F),
                        ],
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.grey[600],
                          blurRadius: 2.0,
                          spreadRadius: 0.0,
                          offset: Offset(
                              2.0, 2.0), // shadow direction: bottom right
                        ),
                      ],
                    ),
                    padding: EdgeInsets.all(15),
                    height: 115,
                    // height: 107,
                    width: double.parse((listaimagens.length * 68).toString()),
                    child: ListView.builder(
                      scrollDirection: Axis.horizontal,
                      itemCount: listaimagens.length,
                      itemBuilder: (context, index) {
                        return _mostraFoto(listaimagens[index], context);
                      },
                    ),
                  ),
                ),
                // Container(
                //   height: 10,
                // ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
