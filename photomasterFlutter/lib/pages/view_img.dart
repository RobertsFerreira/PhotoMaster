import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:photomaster/pages/img_bg.dart';

class ViewImage extends StatefulWidget {
  @override
  _ViewImageState createState() => _ViewImageState();
}

class _ViewImageState extends State<ViewImage> {
  String imagem1;
  String imagem2;
  String imagem3;
  String imagem4;
  String imagemFundo;
  String original;

  List listaimagens = [];

  _recebeLista() async{

    String url = "http://robertferreira.ddns.net:5000/enviarfoto";
    var response = await http.get(url,);
    print(response.body);
  }

  @override
  void initState() {
    super.initState();

    setState(
      () {
        imageCache.clear();
        imagem1 = "http://robertferreira.ddns.net:5000/receberfoto/negativo";
        imagem2 = "http://robertferreira.ddns.net:5000/receberfoto/logaritmo";
        imagem3 = "http://robertferreira.ddns.net:5000/receberfoto/logInverso";
        imagem4 = "http://robertferreira.ddns.net:5000/receberfoto/prewitt";
        original = "http://robertferreira.ddns.net:5000/receberfoto/original";
        imagemFundo = original;

        listaimagens = [
          original,
          imagem1,
          imagem2,
          imagem3,
          imagem4,
        ];
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
                  )),
              onTap: () {
                _popUpImage(imagem, context);
              },
            ),
          ),
          Text(
            imagem.toString().replaceAll(
                "http://robertferreira.ddns.net:5000/receberfoto/", ""),
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
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
          actions: <Widget>[],
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
                    height: 107,
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
                Container(
                  height: 10,
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}