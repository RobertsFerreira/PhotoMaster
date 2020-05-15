import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:photomaster/pages/load_img.dart';

_imagePickerButton(texto, funcao) {
  return FlatButton(
    child: Text(texto),
    onPressed: funcao,
  );
}

_imagePickerFunction(context, imagesource) async {
  File imgFile = await ImagePicker.pickImage(source: imagesource);
  Navigator.pop(context);
  if (imgFile == null) return;
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => LoadImg(
        file: imgFile,
      ),
    ),
  );
}

imagePicker(context) {
  return showDialog(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: Text("Camera ou Galeria?"),
        actions: <Widget>[
          _imagePickerButton(
            "Camera",
            () async {
              _imagePickerFunction(context, ImageSource.camera);
            },
          ),
          _imagePickerButton(
            "Galeria",
            () async {
              _imagePickerFunction(context, ImageSource.gallery);
            },
          ),
        ],
      );
    },
  );
}
