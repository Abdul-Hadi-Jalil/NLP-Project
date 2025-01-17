import 'package:flutter/material.dart';
import 'dart:convert';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'dart:html' as html;

class DownloadFilePage extends StatelessWidget {
  const DownloadFilePage({super.key});

  void downloadFile() {
    String fileContent = 'This is an example file.';
    String fileName = 'example.txt';

    final bytes = utf8.encode(fileContent);
    final blob = html.Blob([bytes]);
    final url = html.Url.createObjectUrlFromBlob(blob);

    final anchor = html.AnchorElement(href: url)
      ..target = 'blank'
      ..download = fileName
      ..click();

    html.Url.revokeObjectUrl(url);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Download File'),
      ),
      body: Container(
        color: Colors.orange,
        child: Center(
          child: ElevatedButton(
            onPressed: () => downloadFile(),
            child: Text('Download File'),
          ),
        ),
      ),
    );
  }
}
