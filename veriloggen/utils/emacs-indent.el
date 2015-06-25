:;exec emacs -batch -l   "$0" -f : "$@" --no-site-file -q  # -*- Emacs-Lisp -*-
;     @emacs -batch -l "%~f0" -f :  %*  --no-site-file -q  & goto :EOF

; indent specified file(s) with emacs indent-region
; http://www.emacswiki.org/emacs/EmacsScripts
; http://www.cslab.pepperdine.edu/warford/BatchIndentationEmacs.html

; http://d.hatena.ne.jp/Nos/20131121/1385027070

(defun : ()
  (dolist (f (nthcdr 5 command-line-args))
    (find-file f)
    ;; (c-set-style "stroustrup")
    (indent-region (point-min) (point-max) nil)
    (untabify (point-min) (point-max))
    (save-buffer))
)
;:EOF
