<?php

namespace frontend\controllers;

use yii\web\controllers;

class TestController extends \yii\web\Controller
{
    public function actionIndex() {
        $data = 'testxxxxxxxxxxx';
        return $this->render('index',[
            'xdata' => $data
        ]);
    }
    
    
}
