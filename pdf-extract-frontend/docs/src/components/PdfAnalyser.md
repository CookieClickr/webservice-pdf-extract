# PdfAnalyser

> PdfAnalyser Component
> Handles sending the selected PDF file to an analysis service.

## Props

| Prop name | Description                  | Type | Values | Default |
| --------- | ---------------------------- | ---- | ------ | ------- |
| file      | The PDF file to be analysed. | File | -      |         |

## Events

| Event name    | Properties                                                                                                                                                                                                          | Description |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| json-response | **filename** `string` - Name of the uploaded PDF file.<br/>**status** `string` - Status message.<br/>**pages** `number` - Number of pages in the PDF.<br/>**extractedText** `string` - Extracted text from the PDF. |

---
