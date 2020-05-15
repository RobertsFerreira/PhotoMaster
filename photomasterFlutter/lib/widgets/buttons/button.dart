import 'package:flutter/material.dart';

class ButtonTelaInicial extends StatelessWidget {
  final IconData icon;
  final String text;
  final Function func;

  ButtonTelaInicial(this.text, this.icon, this.func);
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 60,
      width: 270,
      alignment: Alignment.centerLeft,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          stops: [0.3, 1],
          colors: [
            Color(0xFFF58524),
            Color(0xFFF92B7F),
          ],
        ),
        border: Border.all(color: Colors.white),
        borderRadius: BorderRadius.all(
          Radius.circular(5),
        ),
      ),
      child: FlatButton(
        child: ListTile(
          title: Text(
            text,
            style: TextStyle(
              fontWeight: FontWeight.bold,
              color: Colors.white,
              fontSize: 18.0,
            ),
          ),
          trailing: Icon(
            icon,
            color: Colors.white,
          ),
        ),
        onPressed: func,
      ),
    );
  }
}
