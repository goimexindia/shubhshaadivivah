$recaptcha = new Quform_Element('g-recaptcha-response', 'reCAPTCHA');
$recaptcha->addValidator('required');
$recaptcha->addValidator('recaptcha', array('secretKey' => '6Ld0N3wcAAAAAD42aciPXinfohM5K5R96c9aa4f-'));
$recaptcha->setIsHidden(true);
$form->addElement($recaptcha);