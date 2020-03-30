import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { CustomerService } from '../customer.service';
import { Customer } from '../customer';

@Component({
  selector: 'app-customers-list',
  templateUrl: './customers-list.component.html',
  styleUrls: ['./customers-list.component.css']
})
export class CustomersListComponent implements OnInit {

  customers: Observable<Customer[]>;

  constructor(
    private customerService: CustomerService,
  ) { }

  ngOnInit() {
    this.reloadData();
  }

  deleteCustomers() {
    this.customerService.deleteAll()
      .subscribe(
        data => {
          console.log(data);
          this.reloadData();
        },
        error => console.log('ERROR: ' + error));
  }

  reloadData() {
    this.customers = this.customerService.getCustomersList();
  }

  // updateActive(isActive: boolean) {
  //   this.customerService.updateCustomer(this.customer.id,
  //     { name: this.customer.name, age: this.customer.age, active: isActive })
  //     .subscribe(
  //       data => {
  //         console.log(data);
  //         this.customer = data as Customer;
  //       },
  //       error => console.log(error));
  // }

  // deleteCustomer() {
  //   this.customerService.deleteCustomer(this.customer.id)
  //     .subscribe(
  //       data => {
  //         console.log(data);
  //         this.listComponent.reloadData();
  //       },
  //       error => console.log(error));
  // }
}
