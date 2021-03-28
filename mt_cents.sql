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
   aml.amount_residual
   from account_move_line aml
   left join account_move am on am.id=aml.move_id
   left join account_account aa on aa.id=aml.account_id
   where am.name='DPU/2019/0007';
;; update account_move_line set debit=0.01,  balance=0.01,  debit_cash_basis=0.01,  balance_cash_basis=0.01  where id=888164;
;; update account_move_line set credit=0.01, balance=-0.01, credit_cash_basis=0.01, balance_cash_basis=-0.01 where id=925422;

