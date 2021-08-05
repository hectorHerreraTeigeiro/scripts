;; update reports: move RND to 2 decimals, checking formulas '=' use 'in'
;; update account_move_line set debit=round(debit,2), credit=round(credit,2);
select aml.company_id, am.name, sum(aml.credit) as credit, sum (aml.debit) as debit, (sum(credit)-sum(debit))*10000 as diff
   from account_move_line aml
   left join account_move am on am.id=aml.move_id
   group by aml.company_id, am.name
   having (sum(aml.credit)-sum(aml.debit))*10000<>0;
select aml.company_id, am.name, am.id, aml.id, aa.code, 
   aml.debit, aml.credit, aml.balance, 
   aml.debit_cash_basis, aml.credit_cash_basis, aml.balance_cash_basis, 
   aml.amount_residual, '***' as sep, 
   aml.debit-aml.credit as new_bal
   from account_move_line aml
   left join account_move am on am.id=aml.move_id
   left join account_account aa on aa.id=aml.account_id
   where am.name='TIMP/2019/010198' ;
update account_move_line set balance=debit-credit;
;; update account_move_line set debit=28.27,  balance=28.27,  debit_cash_basis=28.27,  balance_cash_basis=28.27  where id=986754; 
;; update account_move_line set debit=2.72,  balance=2.72,  debit_cash_basis=2.72,  balance_cash_basis=2.72  where id=679761; ok
;; update account_move_line set debit=9.87,  balance=9.87,  debit_cash_basis=9.87,  balance_cash_basis=9.87  where id=679786; ok
;; update account_move_line set debit=1587.65,  balance=1587.65,  debit_cash_basis=1587.65,  balance_cash_basis=1587.65  where id=644425; ok

;; update account_move_line set credit=4.96, balance=-4.96, credit_cash_basis=4.96, balance_cash_basis=-4.96 where id=979597; 

;; update account_move_line set credit=0.01, balance=-0.01, credit_cash_basis=0.01, balance_cash_basis=-0.01 where id=925422;
;; update account_move_line set debit=9.87,  balance=9.87,  debit_cash_basis=9.87,  balance_cash_basis=9.87  where id=679786;
